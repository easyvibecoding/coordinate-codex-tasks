# 提示詞範例

[English](examples.md) · [返回 README](../README.zh-TW.md)

在**目前的主 Task** 貼上提示詞。把中括號內的內容換成你的實際工作與驗收條件；只有你明確要求「另開 Codex Task」時，才會建立獨立 Task。`$coordinate-codex-tasks` 可明示使用這個 skill，但排程喚醒及工具仍取決於 Codex 執行環境。

## 1. 委派一個新 Task，由主 Task 負責驗收

```text
使用 $coordinate-codex-tasks。請另開一個 Codex Task，交辦它完成[具體工作]，範圍限於[檔案或模組]；完成條件是[可檢查的成果或命令]。目前這個 Task 保留整合與驗收責任。請確認新 Task 已開始，並為它建立一個專屬監控排程；依實際成果更新檢查節點，驗收完成後停用排程並向我報告。
```

## 2. 同時委派兩個 Task，分別監控

```text
使用 $coordinate-codex-tasks。請另開兩個 Codex Task：第一個負責[工作 A、範圍、驗收條件]；第二個負責[工作 B、範圍、驗收條件]。兩者不要修改相同檔案。由目前 Task 整合與驗收。每個受託 Task 各有自己的監控排程；一般先用約 15 分鐘間隔，沒有實質變化時保持安靜。請不要把兩個 Task 合併到同一個排程，也不要讓受託 Task 管理排程。
```

## 3. 續接已存在的 Task

```text
使用 $coordinate-codex-tasks。請續接這個既有 Codex Task：[貼上 codex://threads/... 連結]。它原本受託處理[目標]，目前已完成[已驗證的進度]，還需[下一步與驗收條件]。目前 Task 繼續負責驗收。請先讀它的狀態與成果；若已有專屬監控排程，就更新原排程，不要新建重複的 Task 或排程。
```

## 4. 新 Task 交由自己追蹤

```text
使用 $coordinate-codex-tasks。請另開一個獨立的 Codex Task 處理[具體目標與驗收條件]。我會直接在新 Task 追蹤和續談；目前 Task 只需確認它已開始並給我連結，不用替它建立監控排程。
```

## 5. 明確要求不排程的委派

```text
使用 $coordinate-codex-tasks。請另開一個 Codex Task 完成[具體工作與驗收條件]，由目前 Task 負責最後驗收。這次不要建立定時監控排程；請在目前回合使用可用的等待工具追蹤，必要時再讀取受託 Task 的成果。
```

這些提示詞指定工作歸屬與檢查方式，不保證模型會一直在背景執行。排程實際喚醒後能否自動依狀態推進，仍以[驗證紀錄](verification.md)所列的證據為準。
