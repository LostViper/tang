# Re-optimize Chapter 18 Onward Outline Spec

## Why
根据前期剧情优化和新增的人物卡设定，需要重新优化第18章及后续章节的章节小纲。新小纲需要承接四海楼的爆火，平滑过渡到农业与工艺领域，并自然引出长孙皇后气疾发作的剧情。同时，必须在近期章节立刻安排长孙兄弟（长孙冲与长孙涣）的动作，凸显家族撕裂。整体要求遵循起点、番茄等爆款网文模型，做到剧情紧凑、爆点密集、爽感十足（装逼打脸、YY），并融入细腻暧昧的感情线元素。

## What Changes
- **重构第18-29章剧情结构**：将原先杜如晦病重的剧情线替换或后置，将核心爆点转移到**长孙兄弟的冲突打脸**、**救治长孙皇后气疾**以及**李世民听闻历史坦白的终极震撼**。
- **长孙兄弟提前入场与家族施压**：在第18-20章安排长孙家内部施压情节。长孙涣作为非嫡子缺乏话语权，被长孙冲以“长孙家对外只有一个声音”为由，强迫其卖掉四海楼股份并与主角切割，而长孙无忌对此默许。这一压迫直接导致长孙涣暗中彻底倒戈，随后长孙冲的暗算被打脸，制造前期爽点。
- **引入李愔与李恪**：在农业/商业过渡期（第19章）引入蜀王李愔作为搞笑混子投资人，为后续李恪入局打下基础。
- **程咬金功能落地**：在与长孙冲的冲突及皇权试探中，让程咬金发挥“君臣润滑剂”和“精明护短”的作用。
- **长孙皇后气疾与婚约反转**：第21-24章集中处理气疾爆发、蓝星调药、现代医药降维救治，以及长孙皇后态度大变、撕毁长孙冲与长乐婚约的核心爆点。
- **李世民的终极震撼**：第25-26章安排主角与房玄龄向李世民坦白大唐后续历史，促使李世民完成帝王自省并彻底收束储位（确立太子，切断李泰机会）。
- **感情线与基本盘收束**：第27-29章描写李恪李愔彻底归心，主角与长乐、高阳的细腻暧昧互动，完成第一卷“昼治大唐、夜治蓝星”的双线大高潮。

## Impact
- Affected specs: 剧情大纲设计能力、爆款网文节奏控制能力。
- Affected code: `/Users/eric/我带了一整个地球穿越大唐/我带了一整个地球穿越大唐-小说项目/04-剧情大纲/13-第一卷章节小纲.md`（主要修改第18章至第29章的内容）。

## ADDED Requirements
### Requirement: 爆款网文爽点与爆点设计
The system SHALL provide dense explosive points in the outline:
- **WHEN** Zhangsun Chong attempts to suppress the protagonist, **THEN** the protagonist must use dimensional-crush methods (modern knowledge/resources) to thoroughly slap his face.
- **WHEN** Empress Zhangsun suffers an asthma attack, **THEN** traditional doctors must be helpless, highlighting the protagonist's modern medical rescue as a miraculous, status-altering event.
- **WHEN** the history of Tang is revealed, **THEN** Emperor Li Shimin must show extreme shock and undertake profound self-reflection, leading to decisive political actions (securing the Crown Prince).

### Requirement: 细腻暧昧的感情线
The system SHALL integrate subtle, push-and-pull romantic elements:
- **WHEN** interacting with Changle and Gaoyang, **THEN** the interactions must not be vulgar, but filled with tension, curiosity, and emotional shifting, especially after the tearing of the marriage contract.

## MODIFIED Requirements
### Requirement: 章节小纲的平滑过渡
将原本直接切入医药（救治杜如晦）的剧情，修改为：从酒楼爆火 -> 暴露出粮食与物资短缺 -> 引入土豆、红薯、曲辕犁等农业与工艺降维打击 -> 引出皇家农庄/产业视察 -> 突发长孙皇后气疾。
