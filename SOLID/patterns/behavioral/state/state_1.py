from __future__ import annotations
from abc import ABC, abstractmethod


class Order:
    """ Context """

    def __init__(self) -> None:
        self.state: OrderState = PaymentPending(self)

    def pending(self) -> None:
        print('\nTentando executar pending().')
        self.state.pending()

    def approve(self) -> None:
        print('\nTentando executar approve().')
        self.state.approve()

    def reject(self) -> None:
        print('\nTentando executar reject().')
        self.state.reject()


class OrderState(ABC):
    def __init__(self, order: Order) -> None:
        self.order = order

    @abstractmethod
    def pending(self) -> None:
        ...

    @abstractmethod
    def approve(self) -> None:
        ...

    @abstractmethod
    def reject(self) -> None:
        ...

    def __str__(self) -> str:
        return self.__class__.__name__


class PaymentPending(OrderState):
    def pending(self) -> None:
        print('Pagamento já pendente.')

    def approve(self) -> None:
        self.order.state = PaymentApproved(self.order)
        print('Pagamento Aprovado.')

    def reject(self) -> None:
        self.order.state = PaymentReject(self.order)
        print('Pagamento Recusado.')


class PaymentApproved(OrderState):
    def pending(self) -> None:
        self.order.state = PaymentPending(self.order)
        print('Pagamento Pendente.')

    def approve(self) -> None:
        print('Pagamento já aprovado.')

    def reject(self) -> None:
        self.order.state = PaymentReject(self.order)
        print('Pagamento Recusado.')


class PaymentReject(OrderState):
    def pending(self) -> None:
        print('Pagamento Recusado. Não é possível movê-lo para pendente.')

    def approve(self) -> None:
        print('Pagamento Recusado. Não é possível movê-lo para aprovado.')

    def reject(self) -> None:
        print('Pagamento Recusado. Não é possível recusar novamente.')


if __name__ == '__main__':
    order = Order()
    order.pending()
    order.approve()
    order.approve()
    order.pending()
    order.reject()
    order.reject()
    order.pending()
    order.approve()
