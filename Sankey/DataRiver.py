from pyecharts import options as opts
from pyecharts.charts import Sankey

# 数据准备（保持原有结构）
nodes = [
    {"name": "核心层", "itemStyle": {"color": "#1f3d7a"}},
    {"name": "衍生层", "itemStyle": {"color": "#2f5597"}},
    {"name": "增值层", "itemStyle": {"color": "#3f6cb5"}},
    {"name": "兰花种植销售", "itemStyle": {"color": "#0047ab"}},
    {"name": "红兰之旅体验", "itemStyle": {"color": "#0066cc"}},
    {"name": "文旅衍生品销售", "itemStyle": {"color": "#0080ff"}},
    {"name": "技术服务输出", "itemStyle": {"color": "#3399ff"}},
    {"name": "平台交易佣金", "itemStyle": {"color": "#66b3ff"}},
    {"name": "精细加工产品", "itemStyle": {"color": "#99ccff"}},
    {"name": "总营收", "itemStyle": {"color": "#0047ab"}}
]

links = [
    {"source": "核心层", "target": "兰花种植销售", "value": 41.38},
    {"source": "衍生层", "target": "红兰之旅体验", "value": 18.72},
    {"source": "衍生层", "target": "文旅衍生品销售", "value": 12.65},
    {"source": "增值层", "target": "技术服务输出", "value": 10.15},
    {"source": "增值层", "target": "平台交易佣金", "value": 8.25},
    {"source": "增值层", "target": "精细加工产品", "value": 8.85},
    {"source": "兰花种植销售", "target": "总营收", "value": 41.38},
    {"source": "红兰之旅体验", "target": "总营收", "value": 18.72},
    {"source": "文旅衍生品销售", "target": "总营收", "value": 12.65},
    {"source": "技术服务输出", "target": "总营收", "value": 10.15},
    {"source": "平台交易佣金", "target": "总营收", "value": 8.25},
    {"source": "精细加工产品", "target": "总营收", "value": 8.85},
]

# 正确字体配置方案
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
            color="gradient",
            width=1.5
        ),
        label_opts=opts.LabelOpts(
            font_size=12,
            color="#1a365f",
            font_family="Microsoft YaHei",  # 正确位置1：标签字体
            position="inside"
        ),
        node_gap=20
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="业务收入结构分析",
            title_textstyle_opts=opts.TextStyleOpts(
                color="#1a365f",
                font_size=20,
                font_weight="bold",
                font_family="Microsoft YaHei"  # 正确位置2：标题字体
            ),
            pos_left="10%"
        ),
        tooltip_opts=opts.TooltipOpts(
            trigger="item",
            formatter="{b}: {c}%",
            background_color="rgba(255,255,255,0.95)",
            textstyle_opts=opts.TextStyleOpts(
                font_family="Microsoft YaHei",  # 正确位置3：提示框字体
                color="#333"
            )
        )
    )
)

# 生成文件
c.render("DataRiver_sankey.html")