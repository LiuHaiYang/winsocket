unit Unit1;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls, ScktComp, Buttons, ComCtrls;

type
  TForm1 = class(TForm)
    Button1: TButton;
    Button2: TButton;
    Button3: TButton;
    ClientSocket1: TClientSocket;
    Ed_ip: TEdit;
    Label1: TLabel;
    Label2: TLabel;
    Ed_port: TEdit;
    Button4: TButton;
    TabControl1: TTabControl;
    GroupBox1: TGroupBox;
    Memo1: TMemo;
    BitBtn1: TBitBtn;
    procedure Button3Click(Sender: TObject);
    procedure Button1Click(Sender: TObject);
    procedure ClientSocket1Connect(Sender: TObject;
      Socket: TCustomWinSocket);
    procedure ClientSocket1Disconnect(Sender: TObject;
      Socket: TCustomWinSocket);
    procedure ClientSocket1Read(Sender: TObject; Socket: TCustomWinSocket);
    procedure Button2Click(Sender: TObject);
    procedure Button4Click(Sender: TObject);
    procedure BitBtn1Click(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Form1: TForm1;

implementation

{$R *.dfm}

procedure TForm1.Button3Click(Sender: TObject);
begin
  memo1.Lines.Clear;
end;

procedure TForm1.Button1Click(Sender: TObject);
begin
  ClientSocket1.Port := strtointdef(Ed_port.Text, 20000);
  ClientSocket1.Host := Ed_ip.Text;
  ClientSocket1.Open;
end;

procedure TForm1.ClientSocket1Connect(Sender: TObject;
  Socket: TCustomWinSocket);
begin
  memo1.Lines.Add(Socket.RemoteAddress + '连接!');
  button1.Enabled := false;
  button4.Enabled := not button1.Enabled;
  button2.Enabled := true;
end;

procedure TForm1.ClientSocket1Disconnect(Sender: TObject;
  Socket: TCustomWinSocket);
begin
  memo1.Lines.Add(Socket.RemoteAddress + '断开连接!');
  button1.Enabled := true;
  button4.Enabled := not button1.Enabled;
  button2.Enabled := false;
end;

procedure TForm1.ClientSocket1Read(Sender: TObject;
  Socket: TCustomWinSocket);
var
  buf: string;
begin
  buf := Socket.ReceiveText;
  memo1.Lines.Add('收到:' + buf);
  if buf = '[ConnectOK]' then
  begin
    Socket.SendText('[DataFirst]');
  end else if buf = '[DataEnd]' then
  begin

  end else if copy(buf, 1, 6) = '[Data:' then
  begin
    Socket.SendText('[DataNext]');
  end;
end;

procedure TForm1.Button2Click(Sender: TObject);
begin
  if ClientSocket1.Active then
    ClientSocket1.Socket.SendText('DataEmpty]');
end;

procedure TForm1.Button4Click(Sender: TObject);
begin
  ClientSocket1.Close;
end;

procedure TForm1.BitBtn1Click(Sender: TObject);
begin
    Close;
end;

end.

 