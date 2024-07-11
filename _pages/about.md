---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

I am currently a 3rd-Year Master student at [Tsinghua University](https://www.tsinghua.edu.cn/en/), under the guidance of [Prof. Haoqian Wang](https://www.sigs.tsinghua.edu.cn/whq/). I got B.Eng. degree in Measurement and control technology and instruments at [Southeast University](https://www.seu.edu.cn/english/). During my study in [Tsinghua University](https://www.tsinghua.edu.cn/en/), I spent a good time with [Prof. Yebin Liu](https://www.liuyebin.com/) and [Prof. Hanspeter Pfister](https://vcg.seas.harvard.edu/people/hanspeter-pfister).

Currently, my research topic is 3D computer vision, with a particular focus on 3D scene and 3D human reconstruction. (e.g. NeRF, 3D-GS)

[github](https://github.com/minghanqin) / [google scholar](https://scholar.google.com/citations?user=ngEXyLkAAAAJ&hl=en&authuser=1) / [cv](cv.pdf)


# 🔥 News
- *2024.02*: &nbsp;🎉🎉 2 paper accepted to ECCV 2024 !!!
- *2024.02*: &nbsp;🎉🎉 LangSplat has been selected as CVPR 2024 <font color="red"><b>Highlight</b></font> !!!
- *2024.02*: &nbsp;🎉🎉 1 paper accepted to CVPR 2024 !!!
- *2023.11*: &nbsp;🎉🎉 1 paper accepted to AAAI 2024 !!!

# 📝 Publications 

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CVPR 2024 Highlight</div><img src='images/langsplat.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[LangSplat: 3D Language Gaussian Splatting](https://arxiv.org/pdf/2312.16084.pdf)

<b>Minghan Qin\*</b>, [Wanhua Li\*†](https://li-wanhua.github.io/), [Jiawei Zhou\*](https://latitudezhou.github.io/), [Haoqian Wang†](https://www.sigs.tsinghua.edu.cn/whq_en/main.htm), [Hanspeter Pfister](https://seas.harvard.edu/person/hanspeter-pfister)

[**WEBSITE**](https://langsplat.github.io/) [![](https://img.shields.io/github/stars/minghanqin/Langsplat?style=flat-square&label=GitHub%20Star)](https://github.com/minghanqin/LangSplat) <strong><span class='show_paper_citations' data=''></span></strong>
- We introduces LangSplat, which constructs a 3D language field that enables precise and efficient open-vocabulary querying within 3D spaces.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ECCV 2024</div><img src='images/GS-W.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Gaussian in the Wild: 3D Gaussian Splatting for Unconstrained Image Collections](https://arxiv.org/pdf/2403.15704.pdf)

[Dongbin Zhang*](https://github.com/EastbeanZhang), Chuming Wang*, Weitao Wang, [Peihao Li]("https://scholar.google.com/citations?hl=en&user=LYX4AOEAAAAJ"), <b>Minghan Qin</b>, [Haoqian Wang†](https://www.sigs.tsinghua.edu.cn/whq_en/main.htm)
[**Website**](https://eastbeanzhang.github.io/GS-W/) [![](https://img.shields.io/github/stars/eastbeanzhang/Gaussian-Wild?style=flat-square&label=GitHub%20Star)](https://github.com/EastbeanZhang/Gaussian-Wild)
-  We utilize 3D Gaussian Splatting with introduced separated intrinsic and dynamic appearance to reconstruct scenes from uncontrolled images, achieving high-quality results and a 1000 × rendering speed increase.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ECCV 2024</div><img src='images/coders.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Category-level Object Detection, Pose Estimation and Reconstruction from Stereo Images](https://arxiv.org/abs/2407.06984)

[Chuanrui Zhang\*](https://xingyoujun.github.io/), Yonggen Ling\*†, Minglei Lu, <b>Minghan Qin</b>, [Haoqian Wang†](https://www.sigs.tsinghua.edu.cn/whq_en/main.htm)

[**Website**](https://xingyoujun.github.io/coders) [**Datasets**](https://huggingface.co/datasets/xingyoujun/ss3d) [**Code(Coming soon)**]()
-  We present CODERS, a one-stage approach for Category-level Object Detection, pose Estimation and Reconstruction from Stereo images.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">AAAI 2024</div><img src='images/avatarsve.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[High-Fidelity 3D Head Avatars Reconstruction through Spatially-Varying Expression Conditioned Neural Radiance Field](https://arxiv.org/abs/2310.06275)

<b>Minghan Qin\*</b>, Yifan Liu\*, Yuelang Xu, Xiaochen Zhao, [Yebin Liu†](https://www.liuyebin.com/), [Haoqian Wang†](https://www.sigs.tsinghua.edu.cn/whq_en/main.htm)

[**WEBSITE**](https://minghanqin.github.io/AvatarSVE/) <strong><span class='show_paper_citations' data=''></span></strong>
-  We introduce a novel Spatially-Varying Expression (SVE) conditioning, encompassing both spatial positional features and global expression information.
</div>
</div>

# 🎖 Honors and Awards
- Scholarship, [Tsinghua University](https://www.tsinghua.edu.cn/en/), 2023. 
- National 1st Award, [the 10th BD-CASTIC](https://ins.seu.edu.cn/2019/0410/c45116a435789/page.psp), 2019.

# 💻 Research Experience
- *2023.09 - 2024.4*, Harvard University - VCG Lab - Computer Vision Group. I spent a good time with [Prof. Hanspeter Pfister](https://vcg.seas.harvard.edu/people/hanspeter-pfister).
