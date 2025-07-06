from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'task_manager_category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        constraints = [
            models.UniqueConstraint(fields=['name'], name='unique_category_name')
        ]


class Task(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'task_manager_task'
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        ordering = ['-created_at']
        constraints = [
            models.UniqueConstraint(fields=['title'], name='unique_task_title')
        ]


class SubTask(models.Model):
    title = models.CharField(max_length=200, unique=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks')
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'task_manager_subtask'
        verbose_name = 'SubTask'
        verbose_name_plural = 'SubTasks'
        ordering = ['-created_at']
        constraints = [
            models.UniqueConstraint(fields=['title'], name='unique_subtask_title')
        ]
