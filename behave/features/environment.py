import testit


def after_step(context, step):
    if step.status.name == 'failed':
        testit.addAttachments("../resources/attachments/failed.png")
