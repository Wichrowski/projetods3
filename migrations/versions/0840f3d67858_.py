"""empty message

Revision ID: 0840f3d67858
Revises: c30265f78285
Create Date: 2019-06-02 13:26:11.747384

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0840f3d67858'
down_revision = 'c30265f78285'
branch_labels = None
depends_on = None


def upgrade():
    op.execute('COMMIT')
    op.execute('ALTER TYPE tipo_evento ADD VALUE \'Congresso\'')

def downgrade():
    pass
