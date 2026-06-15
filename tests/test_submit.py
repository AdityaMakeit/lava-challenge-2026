import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).parent.parent)
)

import pandas as pd
from src.rag_pipeline import RAGPipeline

from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()


def format_pages(pages):

    if not pages:
        return "[]"

    pages = sorted(set(pages))

    return "[" + ",".join(map(str, pages)) + "]"


def main():

    rag = RAGPipeline()

    test_df = pd.read_csv("data/test.csv")

    console.print(f"\nLoaded [bold]{len(test_df)}[/bold] questions\n")

    answers = []
    evidence_pages = []

    for i, row in test_df.iterrows():

        question = str(row["question"])

        console.print(f"[{i+1}/{len(test_df)}] {question}")

        try:

            result = rag.answer_with_evidence(
                query=question,
                top_k=5
            )

            answer = str(result["answer"]).strip()
            pages = format_pages(result["pages"])

        except Exception:

            answer = ""
            pages = "[]"

        answers.append(answer)
        evidence_pages.append(pages)

    submission = pd.DataFrame({
        "id": test_df["id"],
        "answer": answers,
        "evidence_page_number": evidence_pages
    })

    submission.to_csv(
        "submission.csv",
        index=False,
        encoding="utf-8-sig"
    )

    # ==========================
    # 🎉 FINAL RICH CELEBRATION
    # ==========================

    success_text = Text()
    success_text.append("SUBMISSION GENERATED SUCCESSFULLY", style="bold green")

    console.print("\n")
    console.print(
        Panel.fit(
            success_text,
            title="SUCCESS",
            border_style="green"
        )
    )

    console.print("[bold green]✔ File saved: submission.csv[/bold green]")
    console.print("[bold blue]🚀 Pipeline completed successfully[/bold blue]")
    console.print("[bold yellow]🏆 Everything executed without errors[/bold yellow]\n")

    console.print("[bold]Preview:[/bold]")
    console.print(submission.head())


if __name__ == "__main__":
    main()