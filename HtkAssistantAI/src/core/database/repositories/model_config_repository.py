from core.database.htk_application_database import HtkApplicationDatabase
from core.log.htk_logger import HtkApplicationLogger
from core.models.models_config import ModelConfig

class ModelConfigRepository:

    def __init__(self):
        self._logger = HtkApplicationLogger()
        self._connection = HtkApplicationDatabase.getConnection()
        
    def create_table(self):
        self._logger.log("Creating table model_config")

        with self._connection:
            cursor = self._connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS model_config (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    model_name TEXT NOT NULL,
                    temperature FLOAT,
                    max_token INTEGER,
                    max_retries INTEGER,
                    n INTEGER
                )
            """)
            cursor.close()

    # 🔹 Save (Insert / Update)
    def save(self, model: ModelConfig) -> int:
        with self._connection:
            cursor = self._connection.cursor()
            if model.id is None:
                model_config = self.find_by_name(model.name)
                if model_config is None:
                    cursor.execute("""
                        INSERT INTO model_config
                        (name, model_name, temperature, max_token, max_retries, n)
                        VALUES (?, ?, ?, ?, ?, ?)
                    """, (
                        model.name,
                        model.model_name,
                        model.temperature,
                        model.max_token,
                        model.max_retries,
                        model.n
                    ))
                    model.id = cursor.lastrowid
                else:
                    cursor.execute("""
                    UPDATE model_config SET
                        name = ?,
                        model_name = ?,
                        temperature = ?,
                        max_token = ?,
                        max_retries = ?,
                        n = ?
                    WHERE id = ?
                """, (
                    model.name,
                    model.model_name,
                    model.temperature,
                    model.max_token,
                    model.max_retries,
                    model.n,
                    model_config.id
                ))
                cursor.close()
                return model.id
            else:
                cursor.execute("""
                    UPDATE model_config SET
                        name = ?,
                        model_name = ?,
                        temperature = ?,
                        max_token = ?,
                        max_retries = ?,
                        n = ?
                    WHERE id = ?
                """, (
                    model.name,
                    model.model_name,
                    model.temperature,
                    model.max_token,
                    model.max_retries,
                    model.n,
                    model.id
                ))

            cursor.close()
            return model.id

    
    def find_by_id(self, id: int) -> ModelConfig | None:
        cursor = self._connection.cursor()
        cursor.execute("""
            SELECT id, name, model_name, temperature, max_token, max_retries, n
            FROM model_config WHERE id = ?
        """, (id,))
        row = cursor.fetchone()
        cursor.close()

        return ModelConfig(*row) if row else None
    
    def find_by_name(self, name: str) -> ModelConfig | None:
        cursor = self._connection.cursor()
        cursor.execute("""
            SELECT id, name, model_name, temperature, max_token, max_retries, n
            FROM model_config WHERE name = ?
        """, (name,))
        row = cursor.fetchone()
        cursor.close()

        return ModelConfig(*row) if row else None


    def find_all(self) -> list[ModelConfig]:
        cursor = self._connection.cursor()
        cursor.execute("""
            SELECT id, name, model_name, temperature, max_token, max_retries, n
            FROM model_config
        """)
        rows = cursor.fetchall()
        cursor.close()

        return [ModelConfig(*row) for row in rows]


    def delete(self, id: int):
        with self._connection:
            cursor = self._connection.cursor()
            cursor.execute("DELETE FROM model_config WHERE id = ?", (id,))
            cursor.close()