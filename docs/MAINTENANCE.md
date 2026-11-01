# 目录维护 / Catalog maintenance

中英文 README 的 `catalog:start/end` 之间是完整目录，项目只在这里计数。首屏导航、近期新增表、安装示例、评测记录和官方资源可以再次链接项目，但不会增加总数。

The bilingual README blocks between `catalog:start/end` are the canonical catalog. Navigation, highlights, installation examples, score archives and official-resource links do not add to the count.

## 新增或修改 / Add or update

1. 先按 CONTRIBUTING.md 审查项目。保留历史条目和贡献历史；内容变更同时修改两个 README 的同一分类。
2. 每条采用 `- [owner/repo](https://github.com/owner/repo) - 简介 (⭐N) · 类型`，类型用行尾反引号包裹。类型按已核验功能选择，不能仅因名称含 skill、目录或 MCP 就推断安装形态。
3. 新收录项目在 `data/recent-additions.json` 添加记录：`repo`、真实收录日期 `added_on`、中英文短用途 `zh`/`en`、可核验的收录提交 `commit`。PR 合并后可使用合并提交；直接维护时可先提交目录，再用其 SHA 补充近期记录。不要为凑近期日期改写旧记录。
4. 运行 `python3 scripts/format_catalog.py --write`，按仓库名称排序并生成最近六项。运行 `python3 scripts/refresh_counts.py --write`，更新总数、主目录/生态资源拆分、QC 覆盖率、日期徽章与替代文本。
5. 若新增安装示例，记录资料核验日期、上游入口、平台和付费/服务前置条件，区分资料核验与实际运行测试。不要统一套用未经核验的安装命令。

Update the same category in both READMEs, label the verified project form, and record new inclusions in `data/recent-additions.json` with their real date and commit evidence. A direct catalog update may be committed first, then its SHA used in a follow-up highlight update. The formatter sorts by case-insensitive repository name and renders the latest six records; the count refresher updates both totals and dates.

类型 / Types：`插件` / `Plugin`、`Skill`、`MCP`、`客户端` / `Client`、`模板` / `Template`、`预设` / `Preset`、`工具` / `Tool`、`目录` / `Directory`、`框架` / `Framework`、`资源` / `Resource`、`主题` / `Theme`、`集成` / `Integration`、`复合项目` / `Mixed`。例如管理 Skill 的插件应标 `插件`，不能误标为 Skill 本身。复合项目可以提供多个入口，类型标签不是安装成功的结论。

## 评分 / Scores

现有 82 条分数的来源和缺失字段见 [qc-history.md](qc-history.md)。不要补造历史版本、日期或报告，不要把“不适用”与“未标注”写成 0 分。新评分需保存被测提交/版本、时间、评测器版本、报告链接、运行环境与适用性；仅审查安装资料时不要新增 QC 分数。

See [qc-history.md](qc-history.md) for the original scores and missing evidence. A documentation check is not a new QC run. Preserve evidence before replacing a historical score, and never encode missing/not-applicable assessments as zero.

## 发布前检查 / Before publishing

```sh
python3 scripts/format_catalog.py
python3 scripts/sync_audit.py --summary
python3 scripts/check_markdown.py
python3 scripts/refresh_counts.py
python3 scripts/update_qc_marks.py --check
python3 -m unittest discover -s scripts/tests -v
git diff --check
```

默认检查不会写入 README。`--write` 是明确的修正操作。确认中英文项目、星数、历史分数与类型一致，没有丢失旧条目或添加重复项，再普通推送；远程已前进则先整合、重新验证。线上 Link Check 沿用仓库的容错策略，其成功不代表每个外部服务始终可用。

Checks are read-only unless `--write` is specified. Verify metadata parity and catalog preservation before a normal push. Integrate concurrent remote changes and revalidate. Link Check retains the repository's tolerant policy, so workflow success is not a guarantee that every external service is available.

`scripts/gen_readme.py` 现在是格式维护脚本的兼容入口，不再从临时文件或旧固定分类覆盖整个目录。

`scripts/gen_readme.py` is now a compatibility entry point for the formatter; it no longer overwrites the catalog from temporary data or an obsolete fixed layout.
