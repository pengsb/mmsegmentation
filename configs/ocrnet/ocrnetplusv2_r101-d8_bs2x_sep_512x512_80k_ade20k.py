_base_ = [
    '../_base_/models/ocrnetplusv2_r50-d8_sep.py', '../_base_/datasets/ade20k_bs2x.py',
    '../_base_/default_runtime.py', '../_base_/schedules/schedule_80k_lr2x.py'
]
norm_cfg = dict(type='SyncBN', requires_grad=True)
model = dict(
    pretrained='open-mmlab://resnet101_v1c', 
    backbone=dict(depth=101),
    decode_head=[
        dict(
            type='FCNHead',
            in_channels=1024,
            in_index=2,
            channels=256,
            num_convs=1,
            concat_input=False,
            drop_out_ratio=0.1,
            num_classes=150,
            norm_cfg=norm_cfg,
            align_corners=False,
            loss_decode=dict(
                type='CrossEntropyLoss', use_sigmoid=False, loss_weight=0.4)),
        dict(
            type='DepthwiseSeparableOCRPlusHeadv2',
            in_channels=2048,
            in_index=3,
            channels=512,
            ocr_channels=256,
            c1_in_channels=256,
            c1_channels=48,
            drop_out_ratio=0.1,
            num_classes=150,
            norm_cfg=norm_cfg,
            align_corners=False,
            loss_decode=dict(
                type='CrossEntropyLoss', use_sigmoid=False, loss_weight=1.0))
    ]
)