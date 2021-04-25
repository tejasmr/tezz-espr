from tezz_espr import generate_summary_from_file, generate_summary_from_document

print("Summary of sample.txt from file:\n")
print(generate_summary_from_file('sample.txt', top_n=2))


print("\n\n\nSummary of sample.txt from the extracted string:\n")
file = open('sample.txt', 'r')
file_data = file.readlines()
print(generate_summary_from_document(file_data[0], top_n=2))
