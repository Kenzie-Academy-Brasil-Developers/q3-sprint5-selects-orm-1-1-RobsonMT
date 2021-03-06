"""create models

Revision ID: c30c27870791
Revises: 
Create Date: 2022-04-23 19:43:04.344996

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "c30c27870791"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "grupo_um",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("nome", sa.String(), nullable=False),
        sa.Column("idade", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "grupo_dois",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("nome", sa.String(), nullable=False),
        sa.Column("idade", sa.Integer(), nullable=False),
        sa.Column("conjuge_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["conjuge_id"],
            ["grupo_um.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("conjuge_id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("grupo_dois")
    op.drop_table("grupo_um")
    # ### end Alembic commands ###
