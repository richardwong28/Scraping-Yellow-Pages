import pandas as pd
import os

def clean_and_save(data, filename):
    if not data:
        raise ValueError("Data kosong!")

    df = pd.DataFrame(data)
    df.drop_duplicates(subset=['Name', 'Phone', 'Web', 'Rating'], inplace=True)

    src_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(src_dir)
    output_dir = os.path.join(root_dir, 'output')

    os.makedirs(output_dir, exist_ok=True)

    safe_filename = "".join(c for c in filename if c.isalnum() or c in "._- ").rstrip()
    output_path = os.path.join(output_dir, f"{safe_filename}.csv")

    with open(output_path, 'w', encoding='utf-8-sig', newline='') as f:
        f.write('sep=,\n')  
        df.to_csv(f, index=False)

    print(f"File tersimpan di: {output_path}")
    print(f"Total baris: {len(df)}")
    return output_path