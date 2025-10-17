import os
import sys
import google.generativeai as genai
from dotenv import load_dotenv

# 從 .env 文件加載環境變量
load_dotenv()

# 獲取 API 金鑰
api_key = os.getenv("API_KEY")
if not api_key:
    # 如果找不到 API 金鑰，提示使用者輸入
    print("找不到您的 Google AI API 金鑰。")
    api_key = input("請在此貼上您的 API 金鑰: ").strip()

    # 將金鑰寫入 .env 檔案，以便未來使用
    if api_key:
        with open(".env", "w") as f:
            f.write(f"API_KEY={api_key}\n")
        print("API 金鑰已儲存到 .env 檔案中。")
    else:
        print("錯誤：未提供 API 金鑰。")
        sys.exit(1)

# 設定 Google Generative AI
genai.configure(api_key=api_key)

def generate_poem(topic: str) -> str:
    """
    使用生成式 AI 模型創作一首關於指定主題的五言絕句。

    Args:
        topic: 詩的主題。

    Returns:
        AI 生成的詩。
    """
    model = genai.GenerativeModel('gemini-pro')

    # 精心設計的提示，引導 AI 創作
    prompt = f"請以「{topic}」為主題，創作一首富有詩意的五言絕句。風格請參考唐詩，確保每句五個字，共四句。"

    try:
        response = model.generate_content(prompt)
        # 檢查是否有生成內容
        if response.parts:
            return response.text.strip()
        else:
            return "無法生成詩句，請檢查模型的回應。"

    except Exception as e:
        return f"生成詩句時發生錯誤: {e}"

if __name__ == "__main__":
    # 從命令列參數獲取主題，如果沒有則使用預設主題
    if len(sys.argv) > 1:
        poem_topic = sys.argv[1]
    else:
        poem_topic = "月色"  # 預設主題

    print(f"主題：{poem_topic}\n")
    poem = generate_poem(poem_topic)
    print(poem)