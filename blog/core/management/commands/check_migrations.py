from django.apps import apps
from django.core.management.commands.makemigrations import Command as OriginalCommand


class Command(OriginalCommand):
    def handle(self, *app_labels, **options):
        options["check_changes"] = True
        options["dry_run"] = True

        if app_labels or not options["check_changes"]:
            return super().handle(*app_labels, **options)

        app_labels = {cfg.label for cfg in apps.get_app_configs()}
        return super().handle(*app_labels, **options)
