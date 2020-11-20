# Generated by Django 2.2.3 on 2020-08-25 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0007_auto_20200110_0505'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reportfindinglink',
            options={'ordering': ['report', 'severity__weight', 'position'], 'verbose_name': 'Report finding', 'verbose_name_plural': 'Report findings'},
        ),
        migrations.AlterField(
            model_name='evidence',
            name='caption',
            field=models.CharField(blank=True, help_text='Provide a one line caption to be used in the report - keep it brief', max_length=255, verbose_name='Caption'),
        ),
        migrations.AlterField(
            model_name='evidence',
            name='description',
            field=models.TextField(blank=True, help_text='Describe this evidence to your team', verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='evidence',
            name='friendly_name',
            field=models.CharField(help_text='Provide a simple name to be used to reference this evidence', max_length=255, null=True, verbose_name='Friendly Name'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='description',
            field=models.TextField(blank=True, help_text='Provide a description for this finding that introduces it', null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='finding_guidance',
            field=models.TextField(blank=True, help_text='Provide notes for your team that describes how the finding is intended to be used or editedduring editing', null=True, verbose_name='Finding Guidance'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='host_detection_techniques',
            field=models.TextField(blank=True, help_text='Describe how this finding can be detected on an endpoint - leave blank if this does not apply', null=True, verbose_name='Host Detection Techniques'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='impact',
            field=models.TextField(blank=True, help_text='Describe the impact of this finding on the affected entities', null=True, verbose_name='Impact'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='mitigation',
            field=models.TextField(blank=True, help_text='Describe how this finding can be resolved or addressed', null=True, verbose_name='Mitigation'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='network_detection_techniques',
            field=models.TextField(blank=True, help_text='Describe how this finding can be detected on a network - leave blank if this does not apply', null=True, verbose_name='Network Detection Techniques'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='references',
            field=models.TextField(blank=True, help_text='Provide solid references for this finding, such as links to tools and white papers', null=True, verbose_name='References'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='replication_steps',
            field=models.TextField(blank=True, help_text='Provide an explanation for how the reader may reproduce this finding', null=True, verbose_name='Replication Steps'),
        ),
        migrations.AlterField(
            model_name='finding',
            name='title',
            field=models.CharField(help_text='Enter a title for this finding that will appear in reports', max_length=255, unique=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='findingnote',
            name='note',
            field=models.TextField(blank=True, help_text='Provide additional information about the finding', null=True, verbose_name='Notes'),
        ),
        migrations.AlterField(
            model_name='findingnote',
            name='timestamp',
            field=models.DateField(auto_now_add=True, help_text='Creation timestamp', verbose_name='Timestamp'),
        ),
        migrations.AlterField(
            model_name='findingtype',
            name='finding_type',
            field=models.CharField(help_text='Type of finding (e.g. network)', max_length=255, unique=True, verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='localfindingnote',
            name='note',
            field=models.TextField(blank=True, help_text='Provide additional information about the finding', null=True, verbose_name='Notes'),
        ),
        migrations.AlterField(
            model_name='localfindingnote',
            name='timestamp',
            field=models.DateField(auto_now_add=True, help_text='Creation timestamp', verbose_name='Timestamp'),
        ),
        migrations.AlterField(
            model_name='report',
            name='title',
            field=models.CharField(default='New Report', help_text='Provide a meaningful title for this report - this is only seen in Ghostwriter', max_length=255, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='reportfindinglink',
            name='complete',
            field=models.BooleanField(default=False, help_text='Mark the finding as ready for a QA review', verbose_name='Completed'),
        ),
        migrations.AlterField(
            model_name='reportfindinglink',
            name='finding_guidance',
            field=models.TextField(blank=True, help_text='Provide notes for your team that describes this finding within this report', null=True, verbose_name='Finding Guidance'),
        ),
        migrations.AlterField(
            model_name='reportfindinglink',
            name='position',
            field=models.IntegerField(default=1, verbose_name='Report Position'),
        ),
        migrations.AlterField(
            model_name='reportfindinglink',
            name='references',
            field=models.TextField(blank=True, help_text='Provide solid references for this finding, such as links to reference materials, tooling, and white papers', null=True, verbose_name='References'),
        ),
        migrations.AlterField(
            model_name='reportfindinglink',
            name='title',
            field=models.CharField(help_text='Enter a title for this finding that will appear in the reports', max_length=255, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='severity',
            name='severity',
            field=models.CharField(help_text='Severity rating (e.g. High, Low)', max_length=255, unique=True, verbose_name='Severity'),
        ),
    ]