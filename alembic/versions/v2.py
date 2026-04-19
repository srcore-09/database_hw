from alembic import op
import sqlalchemy as sa

def upgrade():
    op.add_column('authors', sa.Column('birth_year', sa.Integer(), nullable=True))

def downgrade():
    op.drop_column('authors', 'birth_year')
