"""changed Post capacity

Revision ID: f72557bb480d
Revises: b7a0c3787d68
Create Date: 2022-12-20 00:32:26.405448

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f72557bb480d'
down_revision = 'b7a0c3787d68'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.alter_column('body',
               existing_type=sa.VARCHAR(length=140),
               type_=sa.String(length=500),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.alter_column('body',
               existing_type=sa.String(length=500),
               type_=sa.VARCHAR(length=140),
               existing_nullable=True)

    # ### end Alembic commands ###
