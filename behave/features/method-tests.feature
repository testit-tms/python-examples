Feature: method tests

  Scenario: Add links success
    When add links
    Then return true


  Scenario: Add links failed
    When add links
    Then return false


  Scenario: Add attachments success
    When add attachments
    Then return true


  Scenario: Add attachments failed
    When add attachments
    Then return false


  Scenario: Add message success
    When add message
    Then return true


  Scenario: Add message failed
    When add message
    Then return false


  Scenario: Add all methods success
    When add all methods
    Then return true


  Scenario: Add all methods failed
    When add all methods
    Then return false
