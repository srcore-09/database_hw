from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table('publishers',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(length=50), nullable=False)
    )

def downgrade():
    op.drop_table('publishers')
