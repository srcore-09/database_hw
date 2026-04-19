from alembic import op
import sqlalchemy as sa

def upgrade():
    op.drop_table('users')

def downgrade():
    op.create_table('users',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String())
    )
