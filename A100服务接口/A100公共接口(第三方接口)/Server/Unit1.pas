unit Unit1;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls, ScktComp, ExtCtrls, Buttons, ComCtrls;

type
  TForm1 = class(TForm)
    Button1: TButton;
    ServerSocket1: TServerSocket;
    Button2: TButton;
    Timer1: TTimer;
    Button3: TButton;
    Button4: TButton;
    BitBtn1: TBitBtn;
    TabControl1: TTabControl;
    GroupBox1: TGroupBox;
    Memo1: TMemo;
    procedure Button1Click(Sender: TObject);
    procedure ServerSocket1ClientConnect(Sender: TObject;
      Socket: TCustomWinSocket);
    procedure ServerSocket1ClientRead(Sender: TObject;
      Socket: TCustomWinSocket);
    procedure Button2Click(Sender: TObject);
    procedure Button3Click(Sender: TObject);
    procedure ServerSocket1ClientDisconnect(Sender: TObject;
      Socket: TCustomWinSocket);
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

procedure TForm1.Button1Click(Sender: TObject);
begin
  try
    ServerSocket1.Port := 20000;
    ServerSocket1.Active := true;
    memo1.Lines.Add('服务端口已启动！');
    Timer1.Enabled := true;
    Button1.Enabled := false;
    button4.Enabled := not button1.Enabled;
  except
  end;
end;

procedure TForm1.ServerSocket1ClientConnect(Sender: TObject;
  Socket: TCustomWinSocket);
begin
  button2.Enabled := true;
  memo1.Lines.Add(Socket.RemoteHost + '连接!');
  Socket.SendText('[ConnectOK]');
end;

procedure TForm1.ServerSocket1ClientRead(Sender: TObject;
  Socket: TCustomWinSocket);
var
  buf: string;
begin
  buf := Socket.ReceiveText;
  memo1.Lines.Add('收到:' + buf);
  if buf = '[DataTest]' then
  begin
    Socket.SendText('[TestOK]');
  end else if buf = '[DataEnd]' then
  begin

  end else
    Socket.SendText('[DataOK]');

end;

procedure TForm1.Button2Click(Sender: TObject);
var
  i: integer;
begin
  for i := 1 to ServerSocket1.Socket.ActiveConnections do
  begin
    try
      ServerSocket1.Socket.Connections[i - 1].SendText('[DataEmpty]');
    except
      ServerSocket1.Socket.Connections[i - 1].Close;
    end;
  end;
end;

procedure TForm1.Button3Click(Sender: TObject);
begin
  memo1.Lines.Clear;
end;

procedure TForm1.ServerSocket1ClientDisconnect(Sender: TObject;
  Socket: TCustomWinSocket);
begin
  button2.Enabled := false;
  memo1.Lines.Add(Socket.RemoteHost + '断开连接!');
end;

procedure TForm1.Button4Click(Sender: TObject);
begin
  ServerSocket1.Close;
  ServerSocket1.Port := 0;
  button1.Enabled := true;
  button4.Enabled := not button1.Enabled;
end;

procedure TForm1.BitBtn1Click(Sender: TObject);
begin
    Close;
end;

end.

