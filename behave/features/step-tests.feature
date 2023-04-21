Feature: step tests

  Scenario: Steps success
    When step01
    Then return true


  Scenario: Steps failed
    When step01
    Then return false
