import os
import sys
import google.generativeai as genai
from dotenv import load_dotenv

# 從 .env 文件加載環境變量
load_dotenv()

# 獲取 API 金鑰
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("錯誤：請設定您的 API_KEY 環境變數。")
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
    model = genai.GenerativeModel('gemini-2.5-flash')

    # 精心設計的提示，引導 AI 創作出更具藝術性的詩歌
    prompt = f"""
請以「{topic}」為主題，創作一首充滿詩意的五言絕句。
風格請模擬唐代詩人王維，著重於畫面感與意境的融合，詩句需簡潔而意蘊深遠。
請確保詩歌符合以下要求：
1.  每句五個字。
2.  共四句。
3.  風格古典，意境優美。
"""
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
    # 從命令列參數獲取主題，如果沒有則提示使用者輸入
    if len(sys.argv) > 1:
        poem_topic = sys.argv[1]
    else:
        try:
            poem_topic = input("請輸入您想生成詩歌的主題（例如：秋風、星空）：")
            if not poem_topic:
                poem_topic = "月色"  # 如果使用者未輸入任何內容，則使用預設主題
        except EOFError:
            poem_topic = "月色"  # 在非互動式環境中（例如 CI/CD），使用預設主題
            print(f"未檢測到輸入，使用預設主題：{poem_topic}")


    print(f"主題：{poem_topic}\n")
    poem = generate_poem(poem_topic)
    print(poem)