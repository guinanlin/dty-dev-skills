# dty-dev-skills

用于集中管理 Cursor 全局 Skills 的仓库。这个项目的目标是把常用 Skill 统一放在一个可版本化、可共享、可持续维护的 GitHub 仓库中，而不是分散在本地目录里手工维护。

## 项目定位

- 面向对象：Cursor 的全局 Skills（可跨项目复用）。
- 主要价值：统一管理、版本可追溯、便于团队共享、支持自动化校验。
- 使用方式：将该仓库克隆到本地 Skills 目录，让 Cursor 直接加载。

## 推荐目录结构（Monorepo）

建议每个 Skill 单独一个目录，目录内至少包含 `SKILL.md`：

```text
my-global-skills/
├── skill-1/
│   └── SKILL.md
├── skill-2/
│   └── SKILL.md
└── skill-3/
    └── SKILL.md
```

当前仓库就是按这个思路组织（部分目录为符号链接指向外部维护路径）。

## 快速开始

### 1) 克隆到本地 Skills 目录

按你的环境把仓库放到本地 Skills 路径（示例）：

```bash
git clone https://github.com/guinanlin/dty-dev-skills.git ~/.agents/skills
```

如果你使用的是 Cursor 的其他 Skills 路径，也可以克隆到对应目录，只要 Cursor 能读取到即可。

### 2) 日常更新

```bash
cd ~/.agents/skills
git pull
```

### 3) 新增或修改 Skill

```bash
cd ~/.agents/skills
# 新建或编辑某个 skill 目录下的 SKILL.md
git add .
git commit -m "feat: add/update <skill-name>"
git push
```

## 在 Cursor 中怎么用

1. 把 Skill 仓库放到 Cursor 可读取的位置。
2. 每个 Skill 目录内提供清晰的 `SKILL.md`（名称、用途、触发场景、执行步骤）。
3. 在聊天中描述你的目标，Agent 会依据 Skill 描述判断是否调用对应 Skill。

建议在每个 `SKILL.md` 里明确：

- 这个 Skill 解决什么问题；
- 什么输入会触发它；
- 它会执行哪些步骤；
- 输出格式是什么。

## 管理建议（实践版）

- 集中管理：所有全局 Skill 统一在一个仓库维护。
- 便于分享：可按需开放仓库给团队成员复用。
- 自动化：可加入 CI 检查 `SKILL.md` 格式和必填字段。
- 版本治理：为关键版本打 tag（如 `skill-name@v1.0.0`）。
- 定期体检：按月审视 Skill 描述，确保触发条件和执行逻辑仍准确。

## 当前仓库说明

本仓库已推送到：

- <https://github.com/guinanlin/dty-dev-skills>

如果目录中存在符号链接（`symlink`），请确认目标路径在你的机器上可访问；如需纯仓库化管理，建议逐步替换为真实目录并直接纳入本仓库版本控制。
