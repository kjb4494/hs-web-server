from django.db import models


# Create your models here.
class Modifier(models.Model):
    idx = models.AutoField(db_column='idx', primary_key=True)
    description = models.CharField(db_column='description', max_length=255)
    description_ko = models.CharField(db_column='descriptionKo', max_length=255, default='')
    effect_type = models.CharField(db_column='effectType', max_length=63)
    example = models.CharField(db_column='example', max_length=255)
    modifier = models.CharField(db_column='modifier', max_length=127, null=False, unique=True)
    m_type = models.CharField(db_column='mType', max_length=63, null=False)
    version_added = models.CharField(db_column='versionAdded', max_length=15)
    default_value = models.FloatField(db_column='defaultValue')

    class Meta:
        db_table = 'cmbModifier'

    def natural_key(self):
        return {
            'idx': self.idx,
            'name': self.modifier,
            'type': self.m_type,
            'effect_type': self.effect_type,
            'description': self.description,
            'description_ko': self.description_ko,
            'default_value': self.default_value,
            'version_added': self.version_added
        }

    def __str__(self):
        return '{idx}: {modifier}({description})'.format(
            idx=self.idx, modifier=self.modifier, description=self.description
        )
