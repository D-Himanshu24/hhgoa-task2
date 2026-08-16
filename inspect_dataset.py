from datasets import load_dataset

dataset = load_dataset(
    "ai4bharat/MSMARCO-XI",
    data_files={"validation": "validation/hinval.parquet"},
    split="validation",
    streaming=True
)

record = next(iter(dataset))

print("\n--- BASIC INFO ---")
print("Query ID:", record["query_id"])
print("Query type:", record["query_type"])
print("Source language:", record["source_lang"])
print("Target language:", record["target_lang"])

print("\n--- QUERY ---")
print(record["query"])

print("\n--- ANSWER ---")
print(record["Answer"])

print("\n--- PASSAGES ---")

english = record["passages"]["English_passages"]
hindi = record["passages"]["Translated_passages"]
selected = record["passages"]["is_selected"]

for i, (en, hi, flag) in enumerate(zip(english, hindi, selected), start=1):
    print(f"\nPassage {i} | selected={flag}")
    print("Hindi:", hi)
    print("English:", en)