"""adds url_imagem to evento

Revision ID: f4b1f6787d09
Revises: 70750a215ace
Create Date: 2019-06-19 23:56:50.545963

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f4b1f6787d09'
down_revision = '70750a215ace'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('evento', sa.Column('url_imagem', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('evento', 'url_imagem')
    # ### end Alembic commands ###
