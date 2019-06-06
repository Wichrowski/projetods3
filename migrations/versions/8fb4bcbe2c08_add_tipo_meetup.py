"""add_tipo_meetup

Revision ID: 8fb4bcbe2c08
Revises: 907f4313eb44
Create Date: 2019-06-06 20:30:35.256951

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8fb4bcbe2c08'
down_revision = '907f4313eb44'
branch_labels = None
depends_on = None


def upgrade():
    op.execute('COMMIT')
    op.execute("ALTER TYPE tipo_evento ADD VALUE 'Meetup'")
    pass


def downgrade():
    pass
