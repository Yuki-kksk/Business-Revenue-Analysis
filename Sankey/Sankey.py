from pyecharts import options as opts
from pyecharts.charts import Sankey

# 数据准备
nodes = [
    # 层级节点
    {"name": "核心层", "itemStyle": {"color": "#1f3d7a"}},
    {"name": "衍生层", "itemStyle": {"color": "#2f5597"}},
    {"name": "增值层", "itemStyle": {"color": "#3f6cb5"}},

    # 业务板块节点
    {"name": "兰花种植销售", "itemStyle": {"color": "#0047ab"}},
    {"name": "红兰之旅体验", "itemStyle": {"color": "#0066cc"}},
    {"name": "文旅衍生品销售", "itemStyle": {"color": "#0080ff"}},
    {"name": "技术服务输出", "itemStyle": {"color": "#3399ff"}},
    {"name": "平台交易佣金", "itemStyle": {"color": "#66b3ff"}},
    {"name": "精细加工产品", "itemStyle": {"color": "#99ccff"}},

    # 汇总节点
    {"name": "核心层汇总", "itemStyle": {"color": "#1a365f"}},
    {"name": "衍生层汇总", "itemStyle": {"color": "#2a4b7c"}},
    {"name": "增值层汇总", "itemStyle": {"color": "#3a6099"}},
    {"name": "总营收", "itemStyle": {"color": "#0047ab"}}
]

links = [
    # 层级->业务板块
    {"source": "核心层", "target": "兰花种植销售", "value": 41.38},
    {"source": "衍生层", "target": "红兰之旅体验", "value": 18.72},
    {"source": "衍生层", "target": "文旅衍生品销售", "value": 12.65},
    {"source": "增值层", "target": "技术服务输出", "value": 10.15},
    {"source": "增值层", "target": "平台交易佣金", "value": 8.25},
    {"source": "增值层", "target": "精细加工产品", "value": 8.85},

    # 业务板块->层级汇总
    {"source": "兰花种植销售", "target": "核心层汇总", "value": 41.38},
    {"source": "红兰之旅体验", "target": "衍生层汇总", "value": 18.72},
    {"source": "文旅衍生品销售", "target": "衍生层汇总", "value": 12.65},
    {"source": "技术服务输出", "target": "增值层汇总", "value": 10.15},
    {"source": "平台交易佣金", "target": "增值层汇总", "value": 8.25},
    {"source": "精细加工产品", "target": "增值层汇总", "value": 8.85},

    # 层级汇总->总营收
    {"source": "核心层汇总", "target": "总营收", "value": 41.38},
    {"source": "衍生层汇总", "target": "总营收", "value": 31.37},  # 18.72+12.65
    {"source": "增值层汇总", "target": "总营收", "value": 27.25}  # 10.15+8.25+8.85
]

# 可视化配置
c = (
    Sankey(init_opts=opts.InitOpts(
        width="1200px",
        height="800px",
        bg_color="rgba(255,255,255,0)"  # 透明背景
    ))
    .add(
        series_name="",
        nodes=nodes,
        links=links,
        linestyle_opt=opts.LineStyleOpts(
            opacity=0.6,
            curve=0.5,
            color="gradient",  # 渐变效果
            width=1.5
        ),
        label_opts=opts.LabelOpts(
            font_size=12,
            color="#1a365f",
            font_family="Microsoft YaHei",  # 微软雅黑
            position="inside"
        ),
        node_gap=20,
        layout_iterations=100
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="业务收入结构桑基图",
            subtitle="单位：% | 数据来源：财务年报",
            title_textstyle_opts=opts.TextStyleOpts(
                color="#1a365f",
                font_size=20,
                font_family="Microsoft YaHei",
                font_weight="bold"
            ),
            pos_left="10%"
        ),
        tooltip_opts=opts.TooltipOpts(
            trigger="item",
            formatter="{b}: {c}%",
            background_color="rgba(255,255,255,0.95)",
            border_color="#1a365f",
            textstyle_opts=opts.TextStyleOpts(
                font_family="Microsoft YaHei",
                color="#333"
            )
        )
    )
)

# 生成文件
c.render("business_sankey.html")