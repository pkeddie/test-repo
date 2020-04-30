def myDjangoModelMethod(self  ):


    if self.student_id:
        assignments = Assignment.objects.filter(week__in=self.weeks)

        unenrolled_students = Wave.objects.filter(week__in=self.weeks).values_list('unenrolled_students', flat=True)

        # Construct responses based on assignment type
        Assignment.build_assignments_for_weeks(responses, self.assignments, self.students, self.unenrolled_students)
        max_num_assessments = Assessment.build_assessments_for_weeks(self.responses)
        Comment.build_comments_for_weeks(self.responses, self.weeks, self.students, self.unenrolled_students)

    elif self.wave_id:
        assignments = Assignment.objects.filter(week__in=self.weeks)

        unenrolled_students = Wave.objects.filter(week__in=self.weeks).values_list('unenrolled_students', flat=True)

        # Construct responses based on assignment type
        Assignment.build_assignments_for_weeks(self.responses, self.assignments, self.students, self.unenrolled_students)
        max_num_assessments = Assessment.build_assessments_for_weeks(self.responses)
        Comment.build_comments_for_weeks(self.responses, self.weeks, self.students, self.unenrolled_students)

    else:
        # can't happen
        pass
