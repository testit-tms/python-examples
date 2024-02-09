Feature: annotation tests

  Scenario: Without annotation success
    Then return true


  Scenario: Without annotation failed
    Then return false


  @ExternalId=With_external_id_annotation_success
  Scenario: With external id annotation success
    Then return true


  @ExternalId=With_external_id_annotation_failed
  Scenario: With external id annotation failed
    Then return false


  @DisplayName=With_display_name_annotation_success_display_name
  Scenario: With display name annotation success
    Then return true


  @DisplayName=With_display_name_annotation_failed_display_name
  Scenario: With display name annotation failed
    Then return false


  @Title=With_title_annotation_success_title
  Scenario: With title annotation success
    Then return true


  @Title=With_title_annotation_failed_title
  Scenario: With title annotation failed
    Then return false


  @Description=With_description_annotation_success
  Scenario: With description annotation success
    Then return true


  @Description=With_description_annotation_failed
  Scenario: With description annotation failed
    Then return false


  @Labels=Label1,Label2
  Scenario: With labels annotation success
    Then return true


  @Labels=Label1,Label2
  Scenario: With labels annotation failed
    Then return false


  @Links={"url":"https://test01.example","title":"Example01","description":"Example01_description","type":"Issue"}
  @Links={"url":"https://test02.example","title":"Example02","description":"Example02_description","type":"Issue"}
  Scenario: With links annotation success
    Then return true


  @Links={"url":"https://test01.example","title":"Example01","description":"Example01_description","type":"Issue"}
  @Links={"url":"https://test02.example","title":"Example02","description":"Example02_description","type":"Issue"}
  Scenario: With links annotation failed
    Then return false


  @WorkItemIds=30578,30579
  Scenario: With workitemids annotation success
    Then return true


  @WorkItemIds=123,321
  Scenario: With workitemids annotation failed
    Then return false


  @ExternalId=With_all_annotations_success
  @DisplayName=With_all_annotations_success_display_name
  @Title=With_all_annotations_success_title
  @Description=With_all_annotations_success
  @Labels=Label1,Label2
  @Links={"url":"https://test01.example","title":"Example01","description":"Example01_description","type":"Issue"}
  @Links={"url":"https://test02.example","title":"Example02","description":"Example02_description","type":"Issue"}
  @WorkItemIds=30578,30579
  Scenario: With all annotations success
    Then return true


  @ExternalId=With_all_annotations_failed
  @DisplayName=With_all_annotations_failed_display_name
  @Title=With_all_annotations_failed_title
  @Description=With_all_annotations_failed
  @Labels=Label1,Label2
  @Links={"url":"https://test01.example","title":"Example01","description":"Example01_description","type":"Issue"}
  @Links={"url":"https://test02.example","title":"Example02","description":"Example02_description","type":"Issue"}
  @WorkItemIds=123,30579
  Scenario: With all annotations failed
    Then return false


  @ExternalId=parametrized_test_{number}_{value}_success
  @DisplayName=parametrized_test_{number}_{value}_success_display_name
  @Title=parametrized_test_{number}_{value}_success_title
  @Description=parametrized_test_{number}_{value}_success
  Scenario Outline: Parametrized test success
    When get parameters <number> <value>
    Then return true

    Examples:
      | number | value    |
      | 1      | string01 |
      | 2      | string02 |
      | 3      | string03 |


  @ExternalId=parametrized_test_{number}_{value}_failed
  @DisplayName=parametrized_test_{number}_{value}_failed_display_name
  @Title=parametrized_test_{number}_{value}_failed_title
  @Description=parametrized_test_{number}_{value}_failed
  Scenario Outline: Parametrized test failed
    When get parameters <number> <value>
    Then return false

    Examples:
      | number | value    |
      | 1      | string01 |
      | 2      | string02 |
      | 3      | string03 |
