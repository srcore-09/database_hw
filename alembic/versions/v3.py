from alembic import op
import sqlalchemy as sa

def upgrade():
    op.alter_column('authors', 'birth_year', type_=sa.String())

def downgrade():
    op.alter_column('authors', 'birth_year', type_=sa.Integer())
