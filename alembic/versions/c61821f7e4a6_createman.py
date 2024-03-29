"""createman

Revision ID: c61821f7e4a6
Revises: 
Create Date: 2024-02-01 17:13:06.967642

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c61821f7e4a6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('bookid', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('bookname', sa.String(), nullable=True),
    sa.Column('author', sa.String(), nullable=True),
    sa.Column('category', sa.String(), nullable=True),
    sa.Column('publishyear', sa.Integer(), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('bookid')
    )
    op.create_table('user',
    sa.Column('userid', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('dateofbirth', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('userid')
    )
    op.create_table('rentbook',
    sa.Column('rentid', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('bookid', sa.Integer(), nullable=False),
    sa.Column('userid', sa.Integer(), nullable=False),
    sa.Column('dayofrent', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('expirationdate', sa.Date(), nullable=False),
    sa.Column('returnday', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['bookid'], ['book.bookid'], ),
    sa.ForeignKeyConstraint(['userid'], ['user.userid'], ),
    sa.PrimaryKeyConstraint('rentid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rentbook')
    op.drop_table('user')
    op.drop_table('book')
    # ### end Alembic commands ###
