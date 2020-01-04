# I am new to gherkin test. I will try to write some gherkin test for the given use case.
# If I got change to work with this test practices, I can learn quickly.


Feature: Add MultipleChoiceQuestion to a Quitz By a Teacher

    Scenario: Add a Number of MultipleChoice Question in a quitz
        Given Teacher is on Quitz Detail Page where all the questions in a quitz are listed.
        When Teacher clicks add questions
        Then page displays to input multiple choice questions and options
        And
        When Teacher submits the question
        Then Message displayed question added successfully
        And Redirects to question list of that quitz page.


Feature: Answer the quitz by a student

     Scenario: Answer quitz by student
         Given Student is on Quitz page
         When Student clicks start quitz button
         Then questions with options page is displayed
         And
         When Student submits the question
         Then System accepts the partial completion of quitz
         And Redirects to Home page
         And Message displayed quitz subitted successfully



