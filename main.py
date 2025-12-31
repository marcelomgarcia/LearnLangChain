from langchain_community.document_loaders.csv_loader import CSVLoader

def main():
    print("Hello from learnlangchain!")

    loader = CSVLoader(file_path="data/metadata.csv")

    data = loader.load()

    print(data)

if __name__ == "__main__":
    main()
