"""empty message

Revision ID: 7b6ca420bbd4
Revises: ddca1c272cc3
Create Date: 2019-06-04 15:59:08.441424

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b6ca420bbd4'
down_revision = 'ddca1c272cc3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('endereco',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('logradouro', sa.String(), nullable=True),
    sa.Column('id_cidade', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_cidade'], ['cidade.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('evento', sa.Column('id_endereco', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'evento', 'endereco', ['id_endereco'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'evento', type_='foreignkey')
    op.drop_column('evento', 'id_endereco')
    op.drop_table('endereco')
    # ### end Alembic commands ###