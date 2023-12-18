from imports import *
global temp_animations
temp_animations = []

def fadeOut(targetWidget:QWidget, duration=1000, hideit=False, FINISH_HOOK=None, VAL_MAX=0.99, VAL_MIN=0):
    try:
        if targetWidget is None:
            return
        effect = QGraphicsOpacityEffect(targetWidget)
        targetWidget.setGraphicsEffect(effect)
        animation = QPropertyAnimation(effect, b"opacity")

        temp_animations.append(animation) # otherwise it will be garbage collected
        animation.setDuration(duration)
        if not hideit:
            animation.setEndValue(VAL_MAX)
            animation.setStartValue(VAL_MIN)
        else:
            animation.setEndValue(VAL_MIN)
            animation.setStartValue(VAL_MAX)
        # ANIM.setEasingCurve(QEasingCurve.OutBack)
        if FINISH_HOOK != None:
            animation.finished.connect(FINISH_HOOK)
        else:
            def bitti():
                targetWidget.setGraphicsEffect(None)

            animation.finished.connect(bitti)
        animation.start(QAbstractAnimation.DeleteWhenStopped)
    except Exception as err:
        logger.exception(err)

def aniMove(targetWidget:QWidget, dX=0, dY=0, startX=None, startY=None, duration=750, FINISH_HOOK=None,
               EasingCurve=QEasingCurve.OutCubic, PropertyName="pos"):
    try:
        animation = QPropertyAnimation(targetWidget, PropertyName.encode(), duration=duration)
        temp_animations.append(animation)
        animation.setEasingCurve(EasingCurve)
        if startX == None and startY == None:
            if PropertyName == "pos":
                animation.setStartValue(targetWidget.pos())
            else:
                animation.setStartValue(targetWidget.size())
        else:
            if PropertyName == "pos":
                p = targetWidget.pos()
                if startX: p.setX(startX)
                if startY: p.setY(startY)
                animation.setStartValue(p)
            else:
                p = targetWidget.size()
                if startX: p.setWidth(startX)
                if startY: p.setHeight(startY)
                animation.setStartValue(p)

        if PropertyName == "pos":
            wp = targetWidget.pos()
            wp.setX(wp.x() + dX)
            wp.setY(wp.y() + dY)
            animation.setEndValue(wp)
        else:
            wp = targetWidget.size()

            wp.setWidth(wp.width() + dX)
            wp.setHeight(wp.height() + dY)
            animation.setEndValue(wp)
        # ANIM.setEasingCurve(QEasingCurve.OutBack)
        if FINISH_HOOK != None:
            animation.finished.connect(FINISH_HOOK)
        else:
            def bitti():
                targetWidget.setGraphicsEffect(None)

            animation.finished.connect(bitti)
        # print("ANIM: start: ", ANIM.startValue(), " end: ", ANIM.endValue())
        animation.start(QAbstractAnimation.DeleteWhenStopped)

    except Exception as err:
        logger.exception(err)