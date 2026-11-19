"""
CLI Evaluation Script for SQuAD 2.0 Question Answering System.
Runs full evaluation and prints summary metrics table.
"""

import sys
import os
import json
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from src.qa_engine import ExtractiveQAModel
from src.evaluator import SQuADEvaluator
from data.load_dataset import load_squad_file


def main():
    print("=" * 70)
    print("   SQuAD 2.0 Extractive Question Answering System - Evaluation")
    print("=" * 70)

    dataset_path = Path(__file__).resolve().parent / "data" / "squad2_sample.json"
    print(f"[*] Loading SQuAD 2.0 dataset from: {dataset_path}")
    dataset = load_squad_file(str(dataset_path))

    print("[*] Initializing Extractive QA Model...")
    model = ExtractiveQAModel()

    print("[*] Running evaluation across all articles and questions...")
    evaluator = SQuADEvaluator()
    results = evaluator.evaluate_dataset(model, dataset)

    summary = results["summary"]
    print("\n" + "-" * 70)
    print("                    EVALUATION METRICS REPORT")
    print("-" * 70)
    print(f" Total Questions Evaluated: {summary['total_questions']}")
    print(f"   - Answerable Questions:    {summary['has_answer_questions']}")
    print(f"   - Unanswerable (No-Ans):   {summary['no_answer_questions']}")
    print("-" * 70)
    print(f" Exact Match (EM):            {summary['exact_match']:.2f}%")
    print(f" F1 Score:                    {summary['f1_score']:.2f}%")
    print(f" Has-Answer Exact Match:      {summary['has_ans_exact_match']:.2f}%")
    print(f" Has-Answer F1 Score:         {summary['has_ans_f1_score']:.2f}%")
    print(f" No-Answer Accuracy:          {summary['no_ans_accuracy']:.2f}%")
    print("-" * 70)

    print("\nSample Predictions:")
    for i, item in enumerate(results["details"][:8], 1):
        status = "[CORRECT]" if item["exact_match"] == 1.0 else "[PARTIAL/DIFF]"
        print(f"\n{i}. [{item['title']}] {item['question']}")
        print(f"   Ground Truth : {item['ground_truths']}")
        print(f"   Prediction   : {item['prediction']} (Conf: {item['confidence']*100:.1f}%) {status}")
        print(f"   Score        : EM={item['exact_match']}, F1={item['f1']}%")

    # Save output report
    output_path = Path(__file__).resolve().parent / "data" / "evaluation_report.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print(f"\n[*] Detailed report saved to: {output_path}")
    print("=" * 70)


if __name__ == "__main__":
    main()
