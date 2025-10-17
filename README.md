# AI-Powered Chinese Poem Generator (AI 中文詩歌生成器)

這是一個使用 Google Generative AI 技術來創作五言絕句的 Python 專案。現在，你可以透過 AI 的力量，根據你提供的主題，生成富有詩意的古典詩歌。

This project is a Python-based Chinese poem generator that leverages the power of Google's Generative AI to create five-character quatrains. You can now generate poetic verses based on any theme you provide.

## 特色 (Features)

- **AI 驅動**: 採用 Google Gemini 模型，生成更自然、更有意境的詩句。
- **主題自訂**: 可以自由指定詩歌的主題，例如「星空」、「秋風」或「故鄉」。
- **易於使用**: 只需簡單的命令，即可生成一首完整的五言絕句。

## 安裝 (Installation)

1.  **複製儲存庫 (Clone the repository):**
    ```bash
    git clone https://github.com/your-username/Chinese-poems-generator.git
    cd Chinese-poems-generator
    ```

2.  **安裝相依套件 (Install dependencies):**
    ```bash
    pip install -r requirements.txt
    ```

3.  **設定 API 金鑰 (Set up your API Key):**
    -   你需要一個 Google AI 的 API 金鑰。你可以從 [Google AI Studio](https://aistudio.google.com/app/apikey) 獲取。
    -   在專案的根目錄下，建立一個名為 `.env` 的檔案。
    -   在 `.env` 檔案中，加入以下內容，並將 `YOUR_API_KEY` 替換成你的金鑰：
        ```
        API_KEY=YOUR_API_KEY
        ```

## 使用方式 (Usage)

你可以透過命令列直接執行 `main.py` 來生成詩歌。

-   **生成指定主題的詩 (Generate a poem with a specific theme):**
    ```bash
    python main.py "你的主題"
    ```
    例如，生成一首關於「夏日」的詩：
    ```bash
    python main.py "夏日"
    ```

-   **生成預設主題的詩 (Generate a poem with the default theme):**
    如果沒有提供主題，程式會使用預設主題「月色」：
    ```bash
    python main.py
    ```

希望你喜歡用 AI 創作的詩！
Enjoy creating poems with the power of AI!