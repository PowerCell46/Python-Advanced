def gather_credits(needed_credits: int, *tuples):
    courses = []
    collected_credits = 0
    for tuple in tuples:
        if collected_credits >= needed_credits:
            break
        current_course_name = tuple[0]
        current_needed_credits = tuple[1]
        if current_course_name not in courses:
            collected_credits += current_needed_credits
            courses.append(current_course_name)
            
    if collected_credits >= needed_credits:
        return f"Enrollment finished! Maximum credits: {collected_credits}.\nCourses: {', '.join(sorted(courses))}"
    else:
        return f"You need to enroll in more courses! You have to gather {needed_credits - collected_credits} credits more."
