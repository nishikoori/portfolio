# import os
from win32com import client

def convert_docx_to_pdf(docx_path, pdf_path):
    # Wordアプリケーションを起動
    word = client.Dispatch("Word.Application")
    
    # Wordを非表示にする（オプション）
    word.Visible = False

    # 指定したパスのWordファイルを開く
    doc = word.Documents.Open(docx_path)

    # 指定したパスにPDF形式で保存
    doc.SaveAs(pdf_path, FileFormat=17)  # FileFormat=17 はPDF形式を意味する定数

    # ドキュメントを閉じる
    doc.Close()

    # Wordアプリケーションを終了
    word.Quit()

    print(f"変換が完了しました: {pdf_path}")

# 使用例:
docx_path = r"C:\Users\t_nis\OneDrive\デスクトップ\8.23面談実施.docx"  # Wordファイルのパス
pdf_path = r"C:\Users\t_nis\OneDrive\デスクトップ\8.23面談実施.pdf"    # 保存するPDFファイルのパス

convert_docx_to_pdf(docx_path, pdf_path)
