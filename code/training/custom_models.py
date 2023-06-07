import torch
import torch.nn as nn

"""
    CUSTOM RESNET
"""


class CustomResNet(nn.Module):
    def __init__(self, num_classes, layers):
        super(CustomResNet, self).__init__()

        # Initial convolutional layer
        self.conv1 = nn.Conv2d(3, 64, kernel_size=7, stride=2, padding=3, bias=False)
        self.bn1 = nn.BatchNorm2d(64)
        self.relu = nn.ReLU(inplace=True)
        self.maxpool = nn.MaxPool2d(kernel_size=3, stride=2, padding=1)

        # Residual blocks
        layers_list = []
        for i, num_blocks in enumerate(layers):
            stride = 1 if i == 0 else 2
            self.layers_list.append(self._make_layer(
                64 * (2 ** i), 64 * (2 ** (i + 1)), num_blocks, stride=stride
            ))
        self.layers = nn.Sequential(*layers_list)

        # Average pooling and fully connected layer
        self.avgpool = nn.AdaptiveAvgPool2d((1, 1))
        self.fc = nn.Linear(64 * (2 ** len(layers)), num_classes)

    def forward(self, x):
        x = self.conv1(x)
        x = self.bn1(x)
        x = self.relu(x)
        x = self.maxpool(x)

        x = self.layers(x)

        x = self.avgpool(x)
        x = torch.flatten(x, 1)
        x = self.fc(x)

        return x

    def _make_layer(self, in_channels, out_channels, num_blocks, stride=1):
        layers = [ResidualBlock(in_channels, out_channels, stride=stride)]

        # Remaining blocks in the layer
        for _ in range(1, num_blocks):
            layers.append(ResidualBlock(out_channels, out_channels))

        return nn.Sequential(*layers)


class ResidualBlock(nn.Module):
    def __init__(self, in_channels, out_channels, stride=1):
        super(ResidualBlock, self).__init__()

        self.conv1 = nn.Conv2d(in_channels, out_channels, kernel_size=3, stride=stride, padding=1, bias=False)
        self.bn1 = nn.BatchNorm2d(out_channels)
        self.relu = nn.ReLU(inplace=True)
        self.conv2 = nn.Conv2d(out_channels, out_channels, kernel_size=3, stride=1, padding=1, bias=False)
        self.bn2 = nn.BatchNorm2d(out_channels)

        # Shortcut connection when the input and output dimensions differ
        if stride != 1 or in_channels != out_channels:
            self.shortcut = nn.Sequential(
                nn.Conv2d(in_channels, out_channels, kernel_size=1, stride=stride, bias=False),
                nn.BatchNorm2d(out_channels)
            )
        else:
            self.shortcut = nn.Identity()

    def forward(self, x):
        residual = x

        out = self.conv1(x)
        out = self.bn1(out)
        out = self.relu(out)

        out = self.conv2(out)
        out = self.bn2(out)

        out += self.shortcut(residual)
        out = self.relu(out)

        return out





"""
    CUSTOM DENSENET
"""


class CustomDenseNet(nn.Module):
    def __init__(self, num_classes, growth_rate, block_config):
        super(CustomDenseNet, self).__init__()

        self.growth_rate = growth_rate
        self.num_init_features = 2 * growth_rate

        # Initial convolutional layer
        self.conv1 = nn.Conv2d(3, self.num_init_features, kernel_size=7, stride=2, padding=3, bias=False)
        self.bn1 = nn.BatchNorm2d(self.num_init_features)
        self.relu = nn.ReLU(inplace=True)
        self.maxpool = nn.MaxPool2d(kernel_size=3, stride=2, padding=1)

        # Dense blocks
        num_features = self.num_init_features
        self.dense_blocks = nn.ModuleList([])
        self.transition_blocks = nn.ModuleList([])
        self.num_blocks = len(block_config)

        for i, num_blocks in enumerate(block_config):
            dense_block = self._make_dense_block(num_features, num_blocks)
            self.dense_blocks.append(dense_block)

            num_features += num_blocks * growth_rate

            if i != self.num_blocks - 1:
                transition_block = self._make_transition_block(num_features)
                self.transition_blocks.append(transition_block)

                num_features //= 2

        # Batch normalization and fully connected layer
        self.bn_final = nn.BatchNorm2d(num_features)
        self.fc = nn.Linear(num_features, num_classes)

    def forward(self, x):
        x = self.conv1(x)
        x = self.bn1(x)
        x = self.relu(x)
        x = self.maxpool(x)

        for i in range(self.num_blocks):
            x = self.dense_blocks[i](x)

            if i != self.num_blocks - 1:
                x = self.transition_blocks[i](x)

        x = self.bn_final(x)
        x = torch.relu(x)
        x = torch.adaptive_avg_pool2d(x, (1, 1))
        x = torch.flatten(x, 1)
        x = self.fc(x)

        return x

    def _make_dense_block(self, in_channels, num_blocks):
        layers = []

        for _ in range(num_blocks):
            layers.append(DenseBlock(in_channels, self.growth_rate))
            in_channels += self.growth_rate

        return nn.Sequential(*layers)

    def _make_transition_block(self, in_channels):
        return TransitionBlock(in_channels, in_channels // 2)


class DenseBlock(nn.Module):
    def __init__(self, in_channels, growth_rate):
        super(DenseBlock, self).__init__()

        self.relu = nn.ReLU(inplace=True)
        self.bn = nn.BatchNorm2d(in_channels)
        self.conv = nn.Conv2d(in_channels, growth_rate, kernel_size=3, stride=1, padding=1, bias=False)

    def forward(self, x):
        out = self.conv(self.relu(self.bn(x)))
        out = torch.cat([x, out], 1)
        return out


class TransitionBlock(nn.Module):
    def __init__(self, in_channels, out_channels):
        super(TransitionBlock, self).__init__()

        self.relu = nn.ReLU(inplace=True)
        self.bn = nn.BatchNorm2d(in_channels)
        self.conv = nn.Conv2d(in_channels, out_channels, kernel_size=1, stride=1, bias=False)
        self.avgpool = nn.AvgPool2d(kernel_size=2, stride=2)

    def forward(self, x):
        out = self.conv(self.relu(self.bn(x)))
        out = self.avgpool(out)
        return out


"""
    CUSTOM RESNET WITH SEBLOCK
"""


class SEBlock(nn.Module):
    def __init__(self, in_channels, reduction_ratio=16):
        super(SEBlock, self).__init__()

        self.avgpool = nn.AdaptiveAvgPool2d(1)
        self.fc1 = nn.Linear(in_channels, in_channels // reduction_ratio)
        self.relu = nn.ReLU(inplace=True)
        self.fc2 = nn.Linear(in_channels // reduction_ratio, in_channels)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        b, c, _, _ = x.size()

        out = self.avgpool(x).view(b, c)
        out = self.fc1(out)
        out = self.relu(out)
        out = self.fc2(out)
        out = self.sigmoid(out)

        out = out.view(b, c, 1, 1)
        out = x * out

        return out


class BasicBlock(nn.Module):
    expansion = 1

    def __init__(self, in_channels, out_channels, stride=1, reduction_ratio=16):
        super(BasicBlock, self).__init__()

        self.conv1 = nn.Conv2d(
            in_channels, out_channels, kernel_size=3, stride=stride, padding=1, bias=False
        )
        self.bn1 = nn.BatchNorm2d(out_channels)
        self.relu = nn.ReLU(inplace=True)
        self.conv2 = nn.Conv2d(
            out_channels,
            out_channels * self.expansion,
            kernel_size=3,
            stride=1,
            padding=1,
            bias=False,
        )
        self.bn2 = nn.BatchNorm2d(out_channels * self.expansion)
        self.se = SEBlock(out_channels * self.expansion, reduction_ratio)

        if stride != 1 or in_channels != out_channels * self.expansion:
            self.downsample = nn.Sequential(
                nn.Conv2d(
                    in_channels,
                    out_channels * self.expansion,
                    kernel_size=1,
                    stride=stride,
                    bias=False,
                ),
                nn.BatchNorm2d(out_channels * self.expansion),
            )
        else:
            self.downsample = None

    def forward(self, x):
        identity = x

        out = self.conv1(x)
        out = self.bn1(out)
        out = self.relu(out)

        out = self.conv2(out)
        out = self.bn2(out)
        out = self.se(out)

        if self.downsample is not None:
            identity = self.downsample(x)

        out += identity
        out = self.relu(out)

        return out


class CustomSEResNet(nn.Module):
    def __init__(
        self,
        block,
        layers,
        num_classes=1000,
        reduction_ratio=16,
        input_channels=3,
    ):
        super(CustomSEResNet, self).__init__()

        self.in_channels = 64

        self.conv1 = nn.Conv2d(
            input_channels, self.in_channels, kernel_size=7, stride=2, padding=3, bias=False
        )
        self.bn1 = nn.BatchNorm2d(self.in_channels)
        self.relu = nn.ReLU(inplace=True)
        self.maxpool = nn.MaxPool2d(kernel_size=3, stride=2, padding=1)

        self.layers = nn.ModuleList([])
        for i, num_blocks in enumerate(layers):
            stride = 1 if i == 0 else 2
            self.layers.append(self._make_layer(
                block, 64 * (2 ** i), num_blocks, stride, reduction_ratio
            ))

        self.avgpool = nn.AdaptiveAvgPool2d((1, 1))
        self.fc = nn.Linear(64 * (2 ** (len(layers)-1)) * block.expansion, num_classes)

        self.init_weights()

    def _make_layer(self, block, out_channels, blocks, stride=1, reduction_ratio=16):
        layers = []
        layers.append(
            block(
                self.in_channels,
                out_channels,
                stride=stride,
                reduction_ratio=reduction_ratio,
            )
        )
        self.in_channels = out_channels * block.expansion
        for _ in range(1, blocks):
            layers.append(block(self.in_channels, out_channels, reduction_ratio=reduction_ratio))

        return nn.Sequential(*layers)

    def forward(self, x):
        out = self.conv1(x)
        out = self.bn1(out)
        out = self.relu(out)
        out = self.maxpool(out)

        out = self.layers(out)

        out = self.avgpool(out)
        out = torch.flatten(out, 1)
        out = self.fc(out)

        return out

    def init_weights(self):
        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                nn.init.kaiming_normal_(m.weight, mode="fan_out", nonlinearity="relu")
            elif isinstance(m, nn.BatchNorm2d):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 0)
            elif isinstance(m, nn.Linear):
                nn.init.constant_(m.bias, 0)


