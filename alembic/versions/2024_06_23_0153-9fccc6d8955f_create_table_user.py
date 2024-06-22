"""Create table User

Revision ID: 9fccc6d8955f
Revises: 
Create Date: 2024-06-23 01:53:23.571242

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9fccc6d8955f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Users',
    sa.Column('telegram_id', sa.BigInteger(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.Column('fullname', sa.String(length=200), nullable=True),
    sa.Column('nickname', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('telegram_id')
    )
    op.create_index(op.f('ix_Users_telegram_id'), 'Users', ['telegram_id'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_Users_telegram_id'), table_name='Users')
    op.drop_table('Users')
    # ### end Alembic commands ###