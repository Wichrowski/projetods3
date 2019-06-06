"""add_new_areas

Revision ID: 907f4313eb44
Revises: 7b6ca420bbd4
Create Date: 2019-06-06 09:45:52.895180

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '907f4313eb44'
down_revision = '7b6ca420bbd4'
branch_labels = None
depends_on = None


def upgrade():
    op.execute('COMMIT')
    op.execute('ALTER TYPE area_evento ADD VALUE \'Arquitetura\'')
    op.execute('ALTER TYPE area_evento ADD VALUE \'Arte\'')
    op.execute('ALTER TYPE area_evento ADD VALUE \'Ciências Sociais\'')
    op.execute('ALTER TYPE area_evento ADD VALUE \'Comunicação\'')
    op.execute('ALTER TYPE area_evento ADD VALUE \'Design\'')
    op.execute('ALTER TYPE area_evento ADD VALUE \'Direito\'')
    op.execute('ALTER TYPE area_evento ADD VALUE \'Economia\'')
    op.execute('ALTER TYPE area_evento ADD VALUE \'Educação\'')
    op.execute('ALTER TYPE area_evento ADD VALUE \'Engenharia\'')
    op.execute('ALTER TYPE area_evento ADD VALUE \'Gastronomia\'')
    op.execute('ALTER TYPE area_evento ADD VALUE \'Negócios\'')
    op.execute('ALTER TYPE area_evento ADD VALUE \'Saúde\'')
    op.execute('ALTER TYPE area_evento ADD VALUE \'Turismo\'')
    pass


def downgrade():
    pass
