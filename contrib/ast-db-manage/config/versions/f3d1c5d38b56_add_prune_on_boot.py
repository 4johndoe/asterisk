"""add_prune_on_boot

Revision ID: f3d1c5d38b56
Revises: 164abbd708c
Create Date: 2017-08-04 17:31:23.124767

"""

# revision identifiers, used by Alembic.
revision = 'f3d1c5d38b56'
down_revision = '164abbd708c'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ############################# Enums ##############################

    # yesno_values have already been created, so use postgres enum object
    # type to get around "already created" issue - works okay with mysql
    yesno_values = ENUM(*YESNO_VALUES, name=YESNO_NAME, create_type=False)

    op.add_column('ps_contacts', sa.Column('prune_on_boot', yesno_values))


def downgrade():
    op.drop_column('ps_contacts', 'prune_on_boot')
