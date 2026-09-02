import uuid
from dataetime import datetime
from sqlalchemy.orm import Column, String, Numeric, Datetime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.database import Base

class Merchant(Base):
    __tablename__ = 'merchant'


    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, unique=True, nullable=False, index=True)
    default_category=Column(String, nullable=True)

    #One Merchant -> Many Transaction
    transaction = relationship("Transaction", back_populates="merchant", cascade="all, delete-orphan")

class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    merchant_id = Column(UUID(as_uuid=True), ForeignKey("merchants.id"), nullable=False)
    transaction_date = Column(DateTime, default=datetime.utcnow, nullable=False)
    total_amount = Column(Numeric(10, 2), nullable=False)
    payment_method = Column(String, nullable=True)

    # Relationships
    merchant = relationship("Merchant", back_populates="transactions")
    items = relationship("TransactionItem", back_populates="transaction", cascade="all, delete-orphan")

class TransactionItem(Base):
    __tablename__ = 'transaction_item'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    transaction_id = Column(UUID(as_uuid=True), ForeignKey("transactions.id"), nullable=False)
    item_name = Column(String, nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    item_category = Column(String, nullable=True)

    # Many Items -> One Transaction
    transaction = relationship("Transaction", back_populates="items")