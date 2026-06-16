from app.db.base import Base
from app.db.models import ChatMessage, Memory, MemoryProfile, User


def test_database_models_are_registered():
    assert User.__tablename__ == "users"
    assert MemoryProfile.__tablename__ == "memory_profiles"
    assert ChatMessage.__tablename__ == "chat_messages"
    assert Memory.__tablename__ == "memories"
    assert "full_name" in User.__table__.columns.keys()
    assert {"name", "birth_date", "death_date", "biography", "personality", "catchphrases", "is_public"}.issubset(
        MemoryProfile.__table__.columns.keys()
    )

    assert {"users", "memory_profiles", "chat_messages", "memories"}.issubset(
        Base.metadata.tables.keys()
    )
