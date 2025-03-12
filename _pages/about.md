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
# 🤔 About-me

I earned my Master’s degree in Artificial Intelligence from [Tsinghua University](https://www.tsinghua.edu.cn/en/) <img src='./images/thu.png' style='width: 2em;'>, where I conducted research under the supervision of [Prof. Haoqian Wang](https://www.sigs.tsinghua.edu.cn/whq_en/main.htm) and collaborated closely with [Prof. Yebin Liu](https://www.liuyebin.com/) on 3D computer vision. Prior to this, I completed my B.Eng. in Measurement and Control Technology & Instruments at [Southeast University](https://www.seu.edu.cn/english/) <img src='./images/seu.png' style='width: 2em;'>. During my graduate studies, I also had the privilege of visiting [Harvard University](https://www.harvard.edu/) <img src='./images/seas.png' style='width: 1.2em;'> as a research intern, working with [Prof. Hanspeter Pfister](https://vcg.seas.harvard.edu/people/hanspeter-pfister) on computational imaging projects.

I am currently an Researcher at ByteDance <img src='./images/bytedance.png' style='width: 6em;'>, focusing on cutting-edge challenges in generative AI and embodied intelligence. My work bridges 3D vision with real-world applications, particularly in dynamic scene understanding and human-AI interaction.

## Research Directions

Core Expertise: 3D computer vision (NeRF, 3D Gaussian Splatting, multi-view reconstruction).

Emerging Focus: Embodied AI-driven video generation, robot-scene interaction, and physics-aware simulation.

Technical Vision: Building scalable frameworks that connect 3D reconstruction, generative models (video/3D assets), and embodied agents for industrial applications.

## Open Opportunities

I am actively recruiting research interns to collaborate on:

📌 3D Content Creation: 3D Reconstruction, Video Generation, 3D Generation

📌 3D Scene Perception: 3D Foundation Model

📌 Embodied AI: LLM/Vision-Language models for robot interaction, simulation environments

If you are seeking any form of academic cooperation, please feel free to email me at [minghan@bytedance.com](mailto:minghan@bytedance.com).


# 🔥 News
- *2025.02*: &nbsp;🎉🎉 2 paper accepted to CVPR 2025 !!!
- *2024.09*: &nbsp;🎉🎉 1 paper accepted to NeurIPS 2024 !!!
- *2024.07*: &nbsp;🎉🎉 1 paper accepted to ACM MM 2024 !!!
- *2024.02*: &nbsp;🎉🎉 2 paper accepted to ECCV 2024 !!!
- *2024.02*: &nbsp;🎉🎉 LangSplat has been selected as CVPR 2024 <font color="red"><b>Highlight</b></font> !!!
- *2024.02*: &nbsp;🎉🎉 1 paper accepted to CVPR 2024 !!!
- *2023.11*: &nbsp;🎉🎉 1 paper accepted to AAAI 2024 !!!

# 📝 Selected Publications 
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CVPR 2025</div><img src='images/4d_LangSplat.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[4D LangSplat: 4D Language Gaussian Splatting via Multimodal Large Language Models]()

Wanhua Li*, Renping Zhou*, Jiawei Zhou, Yingwei Song, Johannes Herter, <b>Minghan Qin</b>, Gao Huang, Hanspeter Pfister

[![Website](https://img.shields.io/badge/Web-Project-green)]()

<strong><span class='show_paper_citations' data=''></span></strong>
- We present 4D LangSplat, an approach to constructing a dynamic 4D language field in evolving scenes, leveraging Multimodal Large Language Models.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CVPR 2025</div><img src='images/hravatar.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[HRAvatar: High-Quality and Relightable Gaussian Head Avatar](https://eastbeanzhang.github.io/HRAvatar/static/paper/HRAvatar.pdf)

Dongbin Zhang, Yunfei Liu, Lijian Lin, Ye Zhu, Kangjie Chen, <b>Minghan Qin</b>, Yu Li†, Haoqian Wang†

[![Website](https://img.shields.io/badge/Web-Project-green)](https://eastbeanzhang.github.io/HRAvatar/)

<strong><span class='show_paper_citations' data=''></span></strong>
- With monocular video input, HRAvatar reconstructs a high-quality, animatable 3D head avatar that enables realistic relighting effects and simple material editing.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CVPR 2024 Highlight</div><img src='images/langsplat.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[LangSplat: 3D Language Gaussian Splatting](https://arxiv.org/pdf/2312.16084.pdf)

<b>Minghan Qin\*</b>, [Wanhua Li\*†](https://li-wanhua.github.io/), [Jiawei Zhou\*](https://latitudezhou.github.io/), [Haoqian Wang†](https://www.sigs.tsinghua.edu.cn/whq_en/main.htm), [Hanspeter Pfister](https://seas.harvard.edu/person/hanspeter-pfister)

[![Website](https://img.shields.io/badge/Web-Project-green)](https://langsplat.github.io/) [![](https://img.shields.io/github/stars/minghanqin/Langsplat?style=flat-square&label=GitHub%20Star)](https://github.com/minghanqin/LangSplat) <strong><span class='show_paper_citations' data='ngEXyLkAAAAJ:u-x6o8ySG0sC'></span></strong>

<a href="https://trendshift.io/repositories/6471" target="_blank"><img src="https://trendshift.io/api/badge/repositories/6471" alt="minghanqin%2FLangSplat | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a> 
  - We introduces LangSplat, which constructs a 3D language field that enables precise and efficient open-vocabulary querying within 3D spaces.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2024</div><img src='images/hdr_gs.gif' alt="sym" width="80%"></div></div>
<div class='paper-box-text' markdown="1">

[HDR-GS: Efficient High Dynamic Range Novel View Synthesis at 1000x Speed via Gaussian Splatting](https://arxiv.org/pdf/2405.15125)

Yuanhao Cai , Zihao Xiao, Yixun Liang, <b>Minghan Qin</b>, Yulun Zhang, Xiaokang Yang, Yaoyao Liu, Alan Yuille

[![Website](https://img.shields.io/badge/Web-Project-green)](https://github.com/caiyuanhao1998/HDR-GS) [![](https://img.shields.io/github/stars/caiyuanhao1998/HDR-GS?style=flat-square&label=GitHub%20Star)](https://github.com/caiyuanhao1998/HDR-GS)
<strong><span class='show_paper_citations' data=''></span></strong>
- The first 3D Gaussian splatting-based method for high dynamic range imaging
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACM MM 2024</div><img src='images/animatablegaussian.gif' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Animatable 3d gaussian: Fast and high-quality reconstruction of multiple human avatars](https://arxiv.org/pdf/2311.16482)

Yang Liu*, Xiang Huang*, <b>Minghan Qin</b>, Qinwei Lin, Haoqian Wang (* indicates equal contribution)

[![Website](https://img.shields.io/badge/Web-Project-green)](https://jimmyyliu.github.io/Animatable-3D-Gaussian/) [![](https://img.shields.io/github/stars/jimmyYliu/Animatable-3d-Gaussian?style=flat-square&label=GitHub%20Star)](https://github.com/jimmyYliu/Animatable-3d-Gaussian)
<strong><span class='show_paper_citations' data=''></span></strong>
- We propose Animatable 3D Gaussian, a novel neural representation for fast and high-fidelity reconstruction of multiple animatable human avatars, which can animate and render the model at interactive rate.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ECCV 2024</div><img src='images/GS-W.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Gaussian in the Wild: 3D Gaussian Splatting for Unconstrained Image Collections](https://arxiv.org/pdf/2403.15704.pdf)

[Dongbin Zhang\*](https://github.com/EastbeanZhang), Chuming Wang\*, Weitao Wang, [Peihao Li]("https://scholar.google.com/citations?hl=en&user=LYX4AOEAAAAJ"), <b>Minghan Qin</b>, [Haoqian Wang†](https://www.sigs.tsinghua.edu.cn/whq_en/main.htm)

[![Website](https://img.shields.io/badge/Web-Project-green)](https://eastbeanzhang.github.io/GS-W/) [![](https://img.shields.io/github/stars/eastbeanzhang/Gaussian-Wild?style=flat-square&label=GitHub%20Star)](https://github.com/EastbeanZhang/Gaussian-Wild)
-  We utilize 3D Gaussian Splatting with introduced separated intrinsic and dynamic appearance to reconstruct scenes from uncontrolled images, achieving high-quality results and a 1000 × rendering speed increase.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ECCV 2024</div><img src='images/coders.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Category-level Object Detection, Pose Estimation and Reconstruction from Stereo Images](https://arxiv.org/abs/2407.06984)

[Chuanrui Zhang\*](https://xingyoujun.github.io/), Yonggen Ling\*†, Minglei Lu, <b>Minghan Qin</b>, [Haoqian Wang†](https://www.sigs.tsinghua.edu.cn/whq_en/main.htm)

[![Website](https://img.shields.io/badge/Web-Project-green)](https://xingyoujun.github.io/coders) [![Datasets](https://img.shields.io/badge/Web-Datasets-blue)](https://huggingface.co/datasets/xingyoujun/ss3d)
-  We present CODERS, a one-stage approach for Category-level Object Detection, pose Estimation and Reconstruction from Stereo images.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">AAAI 2024</div><img src='images/avatarsve.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[High-Fidelity 3D Head Avatars Reconstruction through Spatially-Varying Expression Conditioned Neural Radiance Field](https://arxiv.org/abs/2310.06275)

<b>Minghan Qin\*</b>, Yifan Liu\*, Yuelang Xu, Xiaochen Zhao, [Yebin Liu†](https://www.liuyebin.com/), [Haoqian Wang†](https://www.sigs.tsinghua.edu.cn/whq_en/main.htm)

[![Website](https://img.shields.io/badge/Web-Project-green)](https://minghanqin.github.io/AvatarSVE/) <strong><span class='show_paper_citations' data=''></span></strong>
-  We introduce a novel Spatially-Varying Expression (SVE) conditioning, encompassing both spatial positional features and global expression information.
</div>
</div>

# 🎖 Honors and Awards
- Scholarship, [Tsinghua University](https://www.tsinghua.edu.cn/en/), 2023. 
- National 1st Award, [the 10th BD-CASTIC](https://ins.seu.edu.cn/2019/0410/c45116a435789/page.psp), 2019.

# 💻 Research Experience
- *2023.09 - 2024.4*, Harvard University - VCG Lab - Computer Vision Group. I spent a good time with [Prof. Hanspeter Pfister](https://vcg.seas.harvard.edu/people/hanspeter-pfister).

# 💁 Academic Service
Reviewers of: CVPR, ECCV, ICCV, NeurIPS, ACM MM, AAAI