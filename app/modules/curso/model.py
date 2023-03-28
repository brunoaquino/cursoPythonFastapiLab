from tortoise import fields, models

class Curso(models.Model):
    __tablename__ = "cursos"

    id = fields.IntField(pk=True, auto_now=True)
    titulo = fields.CharField(max_length=250, null=False)
    descricao = fields.CharField(max_length=250, null=False)
    carga_horaria = fields.IntField(null=False)
    qtd_exercicios = fields.IntField(null=False)

    def __str__(self):
        return self.titulo

    class Meta:
        table = "curso"
        ordering = ["id", "-titulo"]
